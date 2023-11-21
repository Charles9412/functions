library("ISLR2")
library("caret")

myControl <- trainControl(
  method = "cv",
  number = 10,
  summaryFunction = defaultSummary,
  verboseIter = TRUE
)


poly_mod <- function(seeds) {
  plot(x = "Degree", y = "MSE", xlim = c(1, 10), 
       ylim = c(13, 30), main = '10 times validation')
  RMSE_in <- rep(0, 10)
  RMSE_out <- rep(0, 10)
  for (j in 1:length(seeds)) {
    for (i in 1:10) { 
      set.seed(seeds[j])
      permuted <- sample(nrow(Auto))
      df <- Auto[permuted, ]
      split <- round(nrow(Auto) * 0.8)
      train <- df[1:split, ]
      test <- df[(split + 1):nrow(Auto), ]
      
      f <- bquote(mpg ~ poly(horsepower, .(i)))
      model <- train(as.formula(f), data = train, 
                     method = "lm")
#                     trControl = myControl)
      RMSE_in[i] <- (model$results$RMSE)^2
      RMSE_out[i] <- (1/nrow(test)) * sum((test$mpg - predict(model, test))^2)
    }
    lines(x = 1:10, y = RMSE_out, type = "l", col = j, pch = 16, lwd = 2)
  }
}

poly_mod_cv <- function(seeds) {
  plot(x = "Degree", y = "MSE", xlim = c(1, 10), 
       ylim = c(13, 30), main = '10x10 fold')
  RMSE_in <- rep(0, 10)
  RMSE_out <- rep(0, 10)
  for (j in 1:length(seeds)) {
    for (i in 1:10) { 
      set.seed(seeds[j])
      permuted <- sample(nrow(Auto))
      df <- Auto[permuted, ]
      split <- round(nrow(Auto))
      train <- df[1:split, ]
      test <- df[(split + 1):nrow(Auto), ]
      
      f <- bquote(mpg ~ poly(horsepower, .(i)))
      model <- train(as.formula(f), data = train, 
                     method = "lm",
                     trControl = myControl)
      RMSE_in[i] <- (model$results$RMSE)^2
      RMSE_out[i] <- (1/nrow(test)) * sum((test$mpg - predict(model, test))^2)
    }
    lines(x = 1:10, y = RMSE_in, type = "l", col = j, pch = 16, lwd = 2)
  }
}
 
set.seed(50)
poly_mod(rnorm(10, 4, 4))
poly_mod_cv(rnorm(10, 4, 4))


